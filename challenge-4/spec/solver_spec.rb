require 'spec_helper'

RSpec.describe Solver do
  subject { described_class.new.call(table) }

  context "Test case 1" do
    let(:table) do
      [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
      ]
    end

    let(:expected_output) do
      [
        [3, 6, 9],
        [2, 5, 8],
        [1, 4, 7]
      ]
    end

    it { is_expected.to eq(expected_output) }
  end

  context "Test case 2" do
    let(:table) do
      [
        [ 1,  2,  3,  4],
        [ 5,  6,  7,  8],
        [ 9, 10, 11, 12],
        [13, 14, 15, 16]
      ]
    end

    let(:expected_output) do
      [
        [ 4, 8, 12, 16],
        [ 3, 7, 11, 15],
        [ 2, 6, 10, 14],
        [ 1, 5,  9, 13]
      ]
    end

    it { is_expected.to eq(expected_output) }
  end

  context "Test case 3" do
    let(:table) do
      [
        [1, 2],
        [3, 4]
      ]
    end

    let(:expected_output) do
      [
        [2, 4],
        [1, 3]
      ]
    end

    it { is_expected.to eq(expected_output) }
  end

  context "Test case 4" do
    let(:table) { [] }
    let(:expected_output) { [] }

    it { is_expected.to eq(expected_output) }
  end
end
