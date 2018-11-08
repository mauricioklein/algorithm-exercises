require 'spec_helper'

RSpec.describe Solver do
  subject { described_class.new.call(arr, n_rows, n_columns) }

  context "with 4x4 table" do
    let(:arr) { (1..16).to_a }
    let(:n_rows) { 4 }
    let(:n_columns) { 4 }

    it { is_expected.to eq([1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]) }
  end

  context "with 3x4 table" do
    let(:arr) { (1..12).to_a }
    let(:n_rows) { 3 }
    let(:n_columns) { 4 }

    it { is_expected.to eq([1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]) }
  end

  context "with 4x3 table" do
    let(:arr) { (1..12).to_a }
    let(:n_rows) { 4 }
    let(:n_columns) { 3 }

    it { is_expected.to eq([1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]) }
  end

  context "with 2x2 table" do
    let(:arr) { (1..4).to_a }
    let(:n_rows) { 2 }
    let(:n_columns) { 2 }

    it { is_expected.to eq([1, 2, 4, 3]) }
  end

  context "with 1x8 table" do
    let(:arr) { (1..8).to_a }
    let(:n_rows) { 1 }
    let(:n_columns) { 8 }

    it { is_expected.to eq([1, 2, 3, 4, 5, 6, 7, 8]) }
  end

  context "with 8x1 table" do
    let(:arr) { (1..8).to_a }
    let(:n_rows) { 8 }
    let(:n_columns) { 1 }

    it { is_expected.to eq([1, 2, 3, 4, 5, 6, 7, 8]) }
  end

  context "with empty table" do
    let(:arr) { [] }
    let(:n_rows) { 1 }
    let(:n_columns) { 0 }

    it { is_expected.to eq([]) }
  end
end
