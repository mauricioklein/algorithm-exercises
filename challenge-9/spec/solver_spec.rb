require 'spec_helper'

RSpec.describe Solver do
  subject { described_class.new.call(table, n_lines, n_columns) }

  describe "Test case #1" do
    let(:table) do
      [
        [1, 1, 1, 1],
        [1, 2, 2, 1],
        [1, 2, 2, 1],
        [1, 1, 1, 1]
      ]
    end
    let(:n_lines) { 4 }
    let(:n_columns) { 4 }

    let(:expected_result) { 8 }

    it { is_expected.to eq(expected_result) }
  end

  describe "Test case #2" do
    let(:table) do
      [
        [1, 2],
        [3, 4]
      ]
    end
    let(:n_lines) { 2 }
    let(:n_columns) { 2 }

    let(:expected_result) { 10 }

    it { is_expected.to eq(expected_result) }
  end

  describe "Test case #3" do
    let(:table) do
      [
        [1, 2, 2, 1],
        [1, 2, 2, 1]
      ]
    end
    let(:n_lines) { 2 }
    let(:n_columns) { 4 }

    let(:expected_result) { 8 }

    it { is_expected.to eq(expected_result) }
  end

  describe "Test case #4" do
    let(:table) do
      [
        [1, 1],
        [2, 2],
        [2, 2],
        [1, 1]
      ]
    end
    let(:n_lines) { 4 }
    let(:n_columns) { 2 }

    let(:expected_result) { 8 }

    it { is_expected.to eq(expected_result) }
  end

  describe "Test case #4" do
    let(:table) do
      [
        []
      ]
    end
    let(:n_lines) { 1 }
    let(:n_columns) { 0 }

    let(:expected_result) { 0 }

    it { is_expected.to eq(expected_result) }
  end
end
